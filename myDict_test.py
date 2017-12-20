#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'单元测试的练习'

__author__ = 'Jacklee'

# 导入模块
import unittest
from myDict import Dict

class TestDict(unittest.TestCase):
	def setUp(self):
		print('setUp...')

	def tearDown(self):
		print('tearDown...')
	
	def test_init(self):
		d = Dict(a = 1, b = 'Test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'Test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEqual(d['key'], 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertEqual(d.key, 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['a']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.a



if __name__ == '__main__':
	unittest.main()
