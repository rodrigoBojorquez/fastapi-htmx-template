from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError, HTTPException
from presentation import app
from presentation.templates import templates
from icecream import ic

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, ex: RequestValidationError):

    errors = ex.errors()

    # Guardarlos en el state de la request
    request.state.errors = errors

    # Si la solicitud es de HTMX, regresa un fragmento HTML con los errores
    if "HX-Request" in request.headers:
        return templates.TemplateResponse(
            "partials/error_fragment.html",
            {"request": request, "errors": errors},
            status_code=400,
        )
    
    # Para solicitudes no HTMX, regresa un JSON con los errores
    return JSONResponse(
        content={"detail": jsonable_encoder(errors)},
        status_code=400,
    )

@app.exception_handler(HTTPException)
async def not_found_exception_handler(request: Request, ex: HTTPException):

    if ex.status_code == 404:
        return templates.TemplateResponse("partials/not_found_for_modal.html", {"request": request}, status_code=404)

    return templates.TemplateResponse(
        "partials/error_fragment.html",
        {"request": request, "errors": [{"msg": ex.detail}]},
        status_code=ex.status_code,
    )