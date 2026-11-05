"""G0-DATA-002 close comparison for a future two-source check.

v0.1 does not call this during the Massive smoke test. With one vendor,
the report stays SECOND_SOURCE_NOT_TESTED. This module only preserves the
accepted rule so offline tests can lock the boundary.
"""

from __future__ import annotations

from decimal import Decimal
from typing import Optional

PRICE_OK = "PRICE_OK"
PRICE_CHECK = "PRICE_CHECK"
DATA_MISMATCH = "DATA_MISMATCH"
SIGNAL_AMBIGUOUS = "SIGNAL_AMBIGUOUS"
TOLERANCE = Decimal("1.00")


def _money(value: object) -> Decimal:
    if isinstance(value, bool) or not isinstance(value, (int, float, str, Decimal)):
        raise ValueError("price is not a number")
    if isinstance(value, float):
        amount = Decimal(str(value))
    else:
        amount = Decimal(value)
    if not amount.is_finite():
        raise ValueError("price is not finite")
    return amount


def compare_closes(
    price_a: object,
    price_b: object,
    *,
    instrument_a: str,
    instrument_b: str,
    session_a: str,
    session_b: str,
    currency_a: str,
    currency_b: str,
    adjustment_a: str,
    adjustment_b: str,
    pivot: Optional[object] = None,
) -> dict:
    """Compare two aligned USD closes.

    ``<= 1.00`` is PRICE_OK and ``> 1.00`` is PRICE_CHECK. A strict pivot
    straddle adds SIGNAL_AMBIGUOUS and blocks breakout confirmation. Identity
    mismatches are DATA_MISMATCH and do not use the dollar rule.
    """
    identity_ok = (
        instrument_a == instrument_b
        and session_a == session_b
        and currency_a == currency_b == "USD"
        and adjustment_a == adjustment_b
        and bool(instrument_a)
        and bool(session_a)
        and bool(adjustment_a)
    )
    if not identity_ok:
        return {
            "state": DATA_MISMATCH,
            "signal": None,
            "absolute_difference": None,
            "breakout_confirmation": "BLOCKED",
        }

    left = _money(price_a)
    right = _money(price_b)
    difference = abs(left - right)
    state = PRICE_OK if difference <= TOLERANCE else PRICE_CHECK
    signal = None
    breakout = "NO_PIVOT_SUPPLIED"
    if pivot is not None:
        level = _money(pivot)
        left_below = left < level
        right_below = right < level
        left_above = left > level
        right_above = right > level
        if (left_below and right_above) or (right_below and left_above):
            signal = SIGNAL_AMBIGUOUS
            breakout = "BLOCKED"
        else:
            breakout = "NOT_BLOCKED_BY_PIVOT_STRADDLE"
    return {
        "state": state,
        "signal": signal,
        "absolute_difference": format(difference, "f"),
        "breakout_confirmation": breakout,
    }
