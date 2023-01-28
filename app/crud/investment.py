from typing import List, Union

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import false

from app.models import CharityProject, Donation


async def get_not_invested_objects(
    model_in: Union[CharityProject, Donation],
    session: AsyncSession
) -> List[Union[CharityProject, Donation]]:
    db_objects = await session.execute(
        select(
            model_in
        ).where(
            model_in.fully_invested == false()
        ).order_by(
            model_in.create_date
        )
    )
    return db_objects.scalars().all()
