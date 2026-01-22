FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN useradd -m appuser

# Copy only the dependency file to leverage Docker cache
COPY pyproject.toml ./

# Install dependencies
RUN pip install --no-cache-dir .

# Copy the rest of the source
COPY . .

# Optional: Install development dependencies
ARG INSTALL_DEV=false
RUN if [ "$INSTALL_DEV" = "true" ]; then \
      pip install --no-cache-dir pytest; \
    fi

RUN chown -R appuser:appuser /app # modifica dei permessi della cartella /app
USER appuser

## Avvia l'app in exec form per evitare che venga interpretata come shell string
ENTRYPOINT ["python", "calcolatrice.py"]