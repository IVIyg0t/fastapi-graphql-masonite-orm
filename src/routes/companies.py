from calendar import c
from typing import Optional

from fastapi import APIRouter, Request

from models.db.Company import Company

router = APIRouter(prefix="/companies", tags=["companies"])


@router.get("/")
def get_companies():
    return Company.all().serialize()


@router.post("/")
def create_company(
    name: str,
    address: str,
    city: str,
    state: str,
    phone: str,
):
    company = Company.create(dict(name=name, address=address, city=city, state=state, phone=phone))

    return company.id


@router.put("/{id}")
def update_company(
    request: Request,
    id: int,
    name: Optional[str] = None,
    address: Optional[str] = None,
    city: Optional[str] = None,
    state: Optional[str] = None,
    phone: Optional[str] = None,
):

    company = Company.find(id)

    company.name = name or company.name
    company.address = address or company.address
    company.city = city or company.city
    company.state = state or company.state
    company.phone = phone or company.phone

    company.save()

    return company.serialize()


@router.get("/{id}")
def get_company(id):
    return Company.find(id).serialize()


@router.get("/{id}/users")
def get_company_users():
    return Company.find(id).users.serialize()
