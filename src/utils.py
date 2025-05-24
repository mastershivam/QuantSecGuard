def map_limit_to_period(interval, limit):
    if interval in ['1d', '1h', '1wk']:
        if interval == '1h':
            # Rough estimate: 6.5 market hours/day → 390 mins
            days = int(limit / 6.5)
        elif interval == '1wk':
            days = int(limit * 7)
        else:
            days = limit
        return f"{min(days, 730)}d"  # cap at 2 years
    else:
        return 'max'  # fallback


from datetime import datetime, timedelta


def period_to_days(period):
    map_days = {
        '1d': 1,
        '5d': 5,
        '1mo': 30,
        '3mo': 90,
        '6mo': 180,
        '1y': 365,
        '2y': 730,
        '5y': 1825,
        '10y': 3650,
        'ytd': 180,  # Rough guess depending on the month
        'max': 3650  # Use a cap like 10 years
    }
    return map_days.get(period, 180)

def estimate_date_range(period):
    today = datetime.today().date()
    delta = timedelta(days=period_to_days(period))
    start = today - delta
    return start, today



    step = delta_map.get(interval, timedelta(days=1))  # fallback
    start_date = now - step * limit
    return start_date.date(), now.date()

valid_period_interval_map = {
    '1d':   ['1m', '2m', '5m', '15m', '30m', '60m'],
    '5d':   ['1m', '2m', '5m', '15m', '30m', '60m'],
    '1mo':  ['5m', '15m', '30m', '60m', '1d'],
    '3mo':  ['15m', '30m', '60m', '1d'],
    '6mo':  ['30m', '60m', '1d'],
    '1y':   ['1d', '1wk'],
    '2y':   ['1d', '1wk'],
    '5y':   ['1d', '1wk', '1mo'],
    '10y':  ['1d', '1wk', '1mo'],
    'ytd':  ['1d', '1wk'],
    'max':  ['1d', '1wk', '1mo'],
}


def estimate_crypto_date_range(interval, limit):
    now = datetime.now()

    interval_map = {
        '1m': timedelta(minutes=1),
        '3m': timedelta(minutes=3),
        '5m': timedelta(minutes=5),
        '15m': timedelta(minutes=15),
        '30m': timedelta(minutes=30),
        '1h': timedelta(hours=1),
        '2h': timedelta(hours=2),
        '4h': timedelta(hours=4),
        '6h': timedelta(hours=6),
        '8h': timedelta(hours=8),
        '12h': timedelta(hours=12),
        '1d': timedelta(days=1),
        '3d': timedelta(days=3),
        '1w': timedelta(weeks=1),
        '1mo': timedelta(days=30),
    }

    step = interval_map.get(interval, timedelta(minutes=1))
    total_span = step * limit
    start = now - total_span

    # Human-readable duration
    hours = total_span.total_seconds() / 3600
    if hours < 24:
        duration = f"{hours:.1f} hours"
    elif hours < 24 * 7:
        duration = f"{hours / 24:.1f} days"
    else:
        duration = f"{hours / (24 * 7):.1f} weeks"

    return start.date(), now.date(), duration