from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import PreBaseDonationCharity


class Donation(PreBaseDonationCharity):
    user_id = Column(Integer, ForeignKey(
        'user.id',
        name='fk_donation_user_id_user'
    ))
    comment = Column(Text)

    def __repr__(self) -> str:
        return (
            f'user_id: {self.user_id}, '
            f'comment: {self.comment[:15]} , '
            f'{super().__repr__()}'
        )
