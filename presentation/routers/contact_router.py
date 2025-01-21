from fastapi import APIRouter, Request, Depends, status
from fastapi.responses import HTMLResponse, Response
from dependency_injector.wiring import inject, Provide
from container import Container
from icecream import ic
from application.contact.services import ContactService
from application.contact.common import CreateContactRequest
from presentation.templates import templates
from fastapi.exceptions import RequestValidationError

"""
    Endpoints y routeo de los templates de contactos
"""

contact_router = APIRouter()

@contact_router.get("/contact", response_class=HTMLResponse)
@inject
async def contact_list(
    request: Request, 
    service: ContactService = Depends(Provide[Container.contact_service])
):
    query_params = request.query_params

    page = int(query_params.get("page", 1))
    search = query_params.get("search", None)

    contacts = service.list(page, search)

    return templates.TemplateResponse(
        request=request,
        name="contacts/index.html",
        context={"contacts": contacts},
    )

@contact_router.get("/contact/new", response_class=HTMLResponse)
async def new_contact_form(request: Request):
    return templates.TemplateResponse(
        "contacts/contact_form.html",
        {"request": request, "contact": None}
    )

@contact_router.post("/contact", response_class=HTMLResponse)
@inject
async def create_contact(
    request: Request,
    service: ContactService = Depends(Provide[Container.contact_service])
):
    form_data = await request.form()

    try:
        data = CreateContactRequest(
            name=form_data.get("name"),
            email=form_data.get("email"),
            phone_number=form_data.get("phone_number")
        )

        contact = service.add_contact(data)
        return templates.TemplateResponse(
            "contacts/contact_row.html",
            {"request": request, "contact": contact}
        )
    
    except RequestValidationError:
        errors = getattr(request.state, "errors", [])
        return templates.TemplateResponse(
            "contacts/contact_form.html",
            {"request": request, "contact": None,"errors": errors}
        )
    

@contact_router.get("/contact/{id}", response_class=HTMLResponse)
@inject
async def edit_contact_form(
    id: int,
    request: Request,
    service: ContactService = Depends(Provide[Container.contact_service])
):
    contact = service.get_contact(id)
    return templates.TemplateResponse(
        "contacts/contact_form.html",
        context={"request": request, "contact": contact}
    )

@contact_router.get("/contact/{id}/delete", response_class=HTMLResponse)
async def delete_contact_modal(
    id: int,
    request: Request,
):
    return templates.TemplateResponse(
        "partials/confirm_delete_for_modal.html",
        context={
            "request": request,
            "url": f"/contact/{id}",
            "target": f"#contact-{id}",
        }
    )

@contact_router.delete("/contact/{id}")
@inject
async def delete_contact(
    id: int,
    service: ContactService = Depends(Provide[Container.contact_service])
):
    service.delete_contact(id)
    return Response(status_code=status.HTTP_200_OK)

@contact_router.get("/contact/{id}/edit", response_class=HTMLResponse)
@inject
async def edit_contact_form(
    id: int,
    request: Request,
    service: ContactService = Depends(Provide[Container.contact_service])
):
    contact = service.get_contact(id)

    return templates.TemplateResponse(
        "contacts/contact_form.html",
        context={"request": request, "contact": contact}
    )