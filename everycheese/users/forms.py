from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    """Form for creating new users with unique usernames.

    The original implementation attempted to update the parent class'
    ``error_messages`` dictionary in place and stored the return value of
    ``dict.update`` (which is ``None``) on an ``error_message`` attribute.

    Besides leaving an unused ``error_message`` attribute behind, mutating the
    parent's dictionary has the side effect of globally changing the error
    messages for *all* ``UserCreationForm`` usages in the project.  To avoid
    these issues we create a copy of the parent's ``error_messages`` and extend
    it with our custom message.
    """

    error_messages = {
        **forms.UserCreationForm.error_messages,
        "duplicate_username": _(
            "This username has already been taken."
        ),
    }

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(
            self.error_messages["duplicate_username"]
        )
