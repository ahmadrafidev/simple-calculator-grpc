# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63\x61lculator.proto\x12\ncalculator\"(\n\nAddRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"\x1d\n\x0b\x41\x64\x64Response\x12\x0e\n\x06result\x18\x01 \x01(\x05\"-\n\x0fSubtractRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"\"\n\x10SubtractResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\"-\n\x0fMultiplyRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\"\"\n\x10MultiplyResponse\x12\x0e\n\x06result\x18\x01 \x01(\x05\"+\n\rDivideRequest\x12\x0c\n\x04num1\x18\x01 \x01(\x05\x12\x0c\n\x04num2\x18\x02 \x01(\x05\" \n\x0e\x44ivideResponse\x12\x0e\n\x06result\x18\x01 \x01(\x02\" \n\x11SquareRootRequest\x12\x0b\n\x03num\x18\x01 \x01(\x02\"$\n\x12SquareRootResponse\x12\x0e\n\x06result\x18\x01 \x01(\x02\x32\xe0\x02\n\nCalculator\x12\x36\n\x03\x41\x64\x64\x12\x16.calculator.AddRequest\x1a\x17.calculator.AddResponse\x12\x45\n\x08Subtract\x12\x1b.calculator.SubtractRequest\x1a\x1c.calculator.SubtractResponse\x12\x45\n\x08Multiply\x12\x1b.calculator.MultiplyRequest\x1a\x1c.calculator.MultiplyResponse\x12?\n\x06\x44ivide\x12\x19.calculator.DivideRequest\x1a\x1a.calculator.DivideResponse\x12K\n\nSquareRoot\x12\x1d.calculator.SquareRootRequest\x1a\x1e.calculator.SquareRootResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calculator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADDREQUEST']._serialized_start=32
  _globals['_ADDREQUEST']._serialized_end=72
  _globals['_ADDRESPONSE']._serialized_start=74
  _globals['_ADDRESPONSE']._serialized_end=103
  _globals['_SUBTRACTREQUEST']._serialized_start=105
  _globals['_SUBTRACTREQUEST']._serialized_end=150
  _globals['_SUBTRACTRESPONSE']._serialized_start=152
  _globals['_SUBTRACTRESPONSE']._serialized_end=186
  _globals['_MULTIPLYREQUEST']._serialized_start=188
  _globals['_MULTIPLYREQUEST']._serialized_end=233
  _globals['_MULTIPLYRESPONSE']._serialized_start=235
  _globals['_MULTIPLYRESPONSE']._serialized_end=269
  _globals['_DIVIDEREQUEST']._serialized_start=271
  _globals['_DIVIDEREQUEST']._serialized_end=314
  _globals['_DIVIDERESPONSE']._serialized_start=316
  _globals['_DIVIDERESPONSE']._serialized_end=348
  _globals['_SQUAREROOTREQUEST']._serialized_start=350
  _globals['_SQUAREROOTREQUEST']._serialized_end=382
  _globals['_SQUAREROOTRESPONSE']._serialized_start=384
  _globals['_SQUAREROOTRESPONSE']._serialized_end=420
  _globals['_CALCULATOR']._serialized_start=423
  _globals['_CALCULATOR']._serialized_end=775
# @@protoc_insertion_point(module_scope)
