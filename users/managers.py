from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        if password is None:
            raise ValueError('The Passwords must be set')
            
        user=self.create_user(email, password)
        user.is_superuser=True
        user.is_staff=True
        
        if user.is_superuser is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        if user.is_staff is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        user.save()
        return user
    