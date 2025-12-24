# Legnext API Reference

Complete reference for the Legnext API endpoints used in this skill.

## Authentication

All API requests require the `x-api-key` header:

```bash
-H "x-api-key: YOUR_API_KEY"
```

Get your API key from: **https://legnext.ai/app/api-keys**

---

## Base URL

```
https://api.legnext.ai
```

---

## 1. Verify API Key

**GET** `/api/account/balance`

Check API key validity and account balance.

### Headers
```
x-api-key: YOUR_API_KEY
```

### Response
```json
{
    "code": 200,
    "data": {
        "account_id": 862,
        "balance_usd": 7.28,
        "available_credits": 7000,
        "available_points": 280
    },
    "message": "success"
}
```

---

## 2. Create Image Generation Task

**POST** `/api/v1/diffusion`

Submit a text-to-image generation task.

### Headers
```
x-api-key: YOUR_API_KEY
Content-Type: application/json
```

### Request Body
```json
{
  "text": "a beautiful sunset over mountains --v 7 --ar 16:9"
}
```

**Parameters:**
- `text` (string, required): Text prompt with Midjourney parameters (1-8192 characters)

### Response
```json
{
  "job_id": "89fc70ee-0357-4dab-98e7-d3383e2efd1b",
  "status": "pending"
}
```

**Response Fields:**
- `job_id`: Unique identifier for tracking (UUID format)
- `status`: Initial status will be "pending"

### Example
```bash
curl -X POST "https://api.legnext.ai/api/v1/diffusion" \
  -H "x-api-key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "a sunset over mountains --v 7 --ar 16:9"}'
```

---

## 3. Get Task Status

**GET** `/api/v1/job/{job_id}`

Retrieve task status and results.

### Headers
```
x-api-key: YOUR_API_KEY
```

### URL Parameters
- `job_id` (string, required): Task identifier (UUID format)

### Response

**Status values:**

| Status | Description |
|--------|-------------|
| `pending` | Job queued, waiting to process |
| `staged` | Job prepared for processing |
| `processing` | Job currently processing |
| `completed` | Job completed successfully |
| `failed` | Job failed with error |

**Completed response:**
```json
{
    "job_id": "89fc70ee-0357-4dab-98e7-d3383e2efd1b",
    "status": "completed",
    "output": {
        "image_url": "https://cdn.legnext.ai/mj/89fc70ee-0357-4dab-98e7-d3383e2efd1b_grid.png",
        "image_urls": [
            "https://cdn.legnext.ai/temp/1766550282000.png",
            "https://cdn.legnext.ai/temp/1766550280996.png",
            "https://cdn.legnext.ai/temp/1766550283659.png",
            "https://cdn.legnext.ai/temp/1766550282248.png"
        ],
        "seed": "2452171661"
    },
    "meta": {
        "created_at": "2025-12-24T04:24:18Z",
        "ended_at": "2025-12-24T04:24:49Z"
    }
}
```

**Output fields:**
- `image_url`: Four-panel grid image URL
- `image_urls`: Array of 4 individual image URLs
- `seed`: Random seed used (for reproducibility)

**Failed response:**
```json
{
    "job_id": "uuid",
    "status": "failed",
    "error": {
        "code": 400,
        "message": "Error description"
    }
}
```

### Example
```bash
curl -X GET "https://api.legnext.ai/api/v1/job/89fc70ee-0357-4dab-98e7-d3383e2efd1b" \
  -H "x-api-key: YOUR_API_KEY"
```

---

## Complete Workflow

### Step 1: Submit Task
```python
import requests

url = "https://api.legnext.ai/api/v1/diffusion"
headers = {
    "x-api-key": "YOUR_API_KEY",
    "Content-Type": "application/json"
}
payload = {
    "text": "a sunset over mountains --v 7 --ar 16:9"
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()
job_id = result["job_id"]  # Save this for polling
```

### Step 2: Poll for Completion
```python
import time

url = f"https://api.legnext.ai/api/v1/job/{job_id}"
headers = {"x-api-key": "YOUR_API_KEY"}

# Initial wait
time.sleep(10)

# Poll until complete
max_wait = 180  # 3 minutes
elapsed = 10

while elapsed < max_wait:
    response = requests.get(url, headers=headers)
    result = response.json()
    status = result["status"]

    if status == "completed":
        # Success - extract images
        image_url = result["output"]["image_url"]      # Grid
        image_urls = result["output"]["image_urls"]    # Individual
        seed = result["output"]["seed"]
        break

    elif status == "failed":
        # Handle error
        error = result.get("error", {})
        print(f"Error: {error.get('message')}")
        break

    # Wait before next check
    time.sleep(5)
    elapsed += 5
```

### Step 3: Use Results
```python
# Four individual images are available:
for i, url in enumerate(image_urls, 1):
    print(f"Image {i}: {url}")

# Grid image (all 4 in one):
print(f"Grid: {image_url}")

# Seed for reproducibility:
print(f"Seed: {seed}")
```

---

## Recommended Polling Strategy

Based on typical generation time (30-80 seconds):

- **Initial Wait**: 10 seconds before first check
- **Polling Interval**: 5 seconds between checks
- **Timeout**: 180 seconds (3 minutes)

---

## Error Handling

### Common HTTP Status Codes

- `200 OK`: Request successful
- `400 Bad Request`: Invalid prompt or parameters
- `401 Unauthorized`: Invalid or missing API key
- `402 Payment Required`: Insufficient balance (check account balance)
- `429 Too Many Requests`: Rate limit (concurrent limit: 6, others auto-queued)
- `500 Internal Server Error`: Server error

### Error Response Format
```json
{
  "error": {
    "code": 400,
    "message": "Error description"
  }
}
```

### Handling Errors

**Insufficient balance:**
- Response code: 402
- Action: Check balance via `/api/account/balance`
- Top up at: https://legnext.ai

**Invalid API key:**
- Response code: 401
- Action: Verify API key configuration

**Rate limit:**
- Concurrent limit: 6 tasks
- Additional tasks auto-queued
- No action needed

**Need help:**
- Contact: support@legnext.ai

---

## Best Practices

1. **Always validate API key** - Use verify endpoint before generation
2. **Handle timeouts** - Set reasonable timeouts (180s recommended)
3. **Save job IDs** - Store for later retrieval if needed
4. **Download images** - Images have temporary storage
5. **Note seeds** - Save seeds for reproducible results
6. **Check balance** - Monitor usage via balance endpoint

---

## Python Scripts

This skill provides ready-to-use scripts:

1. **verify_api_key.py** - Verify API key and check balance
2. **imagine.py** - Submit image generation task
3. **get_task.py** - Query task status
4. **generate_and_wait.py** - Complete workflow (submit + poll)

All scripts handle authentication and error cases automatically.

---

## Notes

- **Generation time**: Typically 30-80 seconds
- **Image count**: 4 variations per generation
- **Image formats**: Grid (1 image) + Individual (4 images)
- **Storage**: Temporary, download for permanent use
- **Rate limit**: 6 concurrent tasks, others auto-queued
- **Billing**: Point-based, auto-deducted on completion
