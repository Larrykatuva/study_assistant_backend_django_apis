from src.models.authentication_models import Profile


class ProfileService:

    @staticmethod
    def validate_owner_exists(owner):
        return Profile.objects.filter(owner=owner).exists()

    @staticmethod
    def create_profile(**kwargs):
        return Profile.objects.create(**kwargs)

    @staticmethod
    def get_user_profile(owner):
        try:
            return Profile.objects.prefetch_related('owner').get(owner=owner)
        except Profile.DoesNotExist:
            return None

    @staticmethod
    def get_profile_by_id(id):
        try:
            return Profile.objects.prefetch_related('owner').get(pk=id)
        except Profile.DoesNotExist:
            return None

    @staticmethod
    def update_user_profile(owner, **kwargs):
        return Profile.objects.filter(owner=owner).update(**kwargs)

    @staticmethod
    def get_all_profiles():
        return Profile.objects.prefetch_related('owner')
