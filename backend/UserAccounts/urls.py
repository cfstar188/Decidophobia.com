�
    ԇ�eN  �                   �   � d Z ddlmZ ddlmZ ddlmZmZ  edej        j	        �  �         ede�  �         ede�  �        gZ
d	S )
a�  
URL configuration for decidophobia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
�    )�admin)�path�   )�home�loginzadmin/� zlogin/N)�__doc__�django.contribr   �django.urlsr   �viewsr   r   �site�urls�urlpatterns� �    �`/Users/faisalmasalha/Documents/csc301/301proj/Decidophobia.com/decidophobia/decidophobia/urls.py�<module>r      s�   ��� �  !�  �  �  �  �  � � � � � � � � � � � � � � � 	�D��5�:�?�#�#��D��T�N�N��D��5������r   