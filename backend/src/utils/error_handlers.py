from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Union

# Custom exception handlers can be added here
# For now, we'll implement a general error handler

async def general_exception_handler(request: Request, exc: Union[Exception, HTTPException]):
    """
    General exception handler for the application
    """
    if isinstance(exc, HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )

    # For other exceptions, return a 500 error
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred"}
    )

# Additional error handlers can be registered as needed