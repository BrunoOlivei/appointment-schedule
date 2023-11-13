from typing import Optional, Union
from pydantic import BaseModel, Field
from fastapi import Response, status


class ResponseData(BaseModel):
    code: int = Field(None)
    message: str = Field(None)
    success: bool = Field(None)
    data: Optional[Union[dict, list]] = Field(None)


class Responses(Response):
    def ResponseOk(
        data: Optional[Union[dict, list]] = None,
        message: str = "Successfully"
    ):
        response = ResponseData()
        response.code = status.HTTP_200_OK
        response.data = data
        response.success = True
        response.message = message
        return Response(
            content=response.model_dump_json(),
            status_code=status.HTTP_200_OK,
            media_type="application/json"
        )

    def ResponseError(message: str = "Error"):
        response = ResponseData()
        response.code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response.success = False
        response.message = message
        return response
    
    def ResponseBadRequest(message: str = "Bad Request"):
        response = ResponseData()
        response.code = status.HTTP_400_BAD_REQUEST
        response.success = False
        response.message = message
        return response
