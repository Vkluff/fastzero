# FastZero

FastZero is a FastAPI-based project that provides a simple API with rate-limited endpoints. It includes a profile endpoint that fetches a random cat fact and displays user information.

## GitHub Repository

[FastZero GitHub Repository](https://github.com/your-repo-link)

## Setup Instructions

Follow these steps to set up and run the project locally:

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-link.git
   cd fastzero
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add the following environment variables:
   ```
   EMAIL=your_email@example.com
   NAME=Your Name
   STACK=Your Tech Stack
   ```

### Running the Application Locally

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

2. Open your browser and navigate to:
   - API root: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Dependencies

The project uses the following dependencies:

- `annotated-types==0.7.0`
- `anyio==4.11.0`
- `certifi==2025.10.5`
- `charset-normalizer==3.4.4`
- `click==8.3.0`
- `Deprecated==1.2.18`
- `fastapi==0.119.0`
- `h11==0.16.0`
- `idna==3.11`
- `limits==5.6.0`
- `packaging==25.0`
- `pydantic==2.12.2`
- `pydantic_core==2.41.4`
- `python-dotenv==1.1.1`
- `requests==2.32.5`
- `slowapi==0.1.9`
- `sniffio==1.3.1`
- `starlette==0.48.0`
- `typing-inspection==0.4.2`
- `typing_extensions==4.15.0`
- `urllib3==2.5.0`
- `uvicorn==0.37.0`
- `wrapt==1.17.3`

Install them using:
```bash
pip install -r requirements.txt
```

## Environment Variables

The following environment variables are required:

- `EMAIL`: Your email address.
- `NAME`: Your name.
- `STACK`: Your tech stack or role.

Define these in a `.env` file in the project root.
