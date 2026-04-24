# Locust Performance Testing — Petstore API

Performance test suite built with Locust against the [Swagger Petstore API](https://petstore.swagger.io).

## What I tested
- `GET /v2/pet/findByStatus?status=available`
- `GET /v2/pet/1`
- `GET /v2/store/inventory`

## Key Findings

| Users | RPS | Failure Rate | 95th Percentile |
|-------|-----|-------------|-----------------|
| 10 | 4.6 | 0% | 150ms |
| 100 | 26.7 | 15% | 320ms |

**Breaking point:** `GET /v2/pet/1` starts failing at ~100 concurrent users with a 44% failure rate.

**Root cause:** High payload response on `findByStatus` (~100KB) combined with concurrent load causes the server to drop single-pet lookups.

## Run Locally

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install locust
export LOCUST_HOST=https://petstore.swagger.io
locust
```

Open **http://localhost:8089**

Start with 10 users, ramp up 2/second. Increase to 100 to see degradation.

## Stack
- Python 3.11
- Locust 2.43.4