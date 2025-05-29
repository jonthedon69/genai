pip install langchain pydantic wikipedia

from typing import Optional

from pydantic import BaseModel, Field, ValidationError

import wikipedia

class InstitutionDetails(BaseModel):

    name: str = Field(description="Name of the institution")

    founder: Optional[str] = Field(description="Founder of the institution")

    founding_year: Optional[int] = Field(description="Year the institution was founded")

    branches: Optional[int] = Field(description="Number of branches of the institution")

    employees: Optional[int] = Field(description="Number of employees in the institution")

    summary: Optional[str] = Field(description="Summary of the institution")

def fetch_institution_details(institution_name: str) -> InstitutionDetails:

    try:

        page = wikipedia.page(institution_name)

        summary = wikipedia.summary(institution_name, sentences=3)

        details = {

        "name": institution_name,

        "founder": None, 

        "founding_year": None, 

        "branches": None, 

        "employees": None, 

        "summary": summary,

        }

        return InstitutionDetails(**details)

    except wikipedia.exceptions.PageError:

        return InstitutionDetails(name=institution_name, summary="No Wikipedia page found.")

    except wikipedia.exceptions.DisambiguationError:

        return InstitutionDetails(name=institution_name, summary="Multiple matches found. Please specify.")

    except ValidationError as e:

        print(f"Validation Error: {e}")

        return InstitutionDetails(name=institution_name, summary="Error parsing details.")

if __name__ == "__main__":

    institution_name = input("Enter the institution name: ")

    details = fetch_institution_details(institution_name)

    print(details)

