def handle_exception(e: Exception) -> dict:
    """
    Converts exceptions into structured error messages.
    """
    return {"error": str(e)}
