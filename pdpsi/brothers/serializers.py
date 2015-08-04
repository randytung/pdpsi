#!/usr/bin/env python

from brothers.models import PClass, Brother
from rest_framework import serializers
from django.contrib.auth.models import User


class BrotherSerializer(serializers.ModelSerializer):
	pledge_class = serializers.ReadOnlyField(source='pledge_class.class_name')
	class Meta:
		model = Brother
		fields = ('name', 'pledge_class', 'pledge_name', 'line_number', 'active')

class PClassSerializer(serializers.ModelSerializer):
	brothers = BrotherSerializer(many=True, read_only=True)
	class Meta:
		model = PClass
		fields = ('class_name', 'year_crossed', 'brothers')

