# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0btypes.proto\x12\x06gs.rpc\x1a\x19google/protobuf/any.proto\"/\n\tQueryArgs\x12\"\n\x04\x61rgs\x18\x01 \x03(\x0b\x32\x14.google.protobuf.Any*0\n\x0b\x43lusterType\x12\t\n\x05HOSTS\x10\x00\x12\x07\n\x03K8S\x10\x01\x12\r\n\tUNDEFINED\x10\x64*\xaa\x02\n\x08\x44\x61taType\x12\r\n\tNULLVALUE\x10\x00\x12\x08\n\x04INT8\x10\x01\x12\t\n\x05INT16\x10\x02\x12\t\n\x05INT32\x10\x03\x12\t\n\x05INT64\x10\x04\x12\n\n\x06INT128\x10\x05\x12\t\n\x05UINT8\x10\x06\x12\n\n\x06UINT16\x10\x07\x12\n\n\x06UINT32\x10\x08\x12\n\n\x06UINT64\x10\t\x12\x0b\n\x07UINT128\x10\n\x12\x07\n\x03INT\x10\x0b\x12\x08\n\x04LONG\x10\x0c\x12\x0c\n\x08LONGLONG\x10\r\x12\x08\n\x04UINT\x10\x0e\x12\t\n\x05ULONG\x10\x0f\x12\r\n\tULONGLONG\x10\x10\x12\t\n\x05\x46LOAT\x10\x12\x12\n\n\x06\x44OUBLE\x10\x13\x12\x0b\n\x07\x42OOLEAN\x10\x14\x12\n\n\x06STRING\x10\x15\x12\x0c\n\x08\x44\x41TETIME\x10\x16\x12\x08\n\x04LIST\x10\x17\x12\x0f\n\x07INVALID\x10\xff\xff\xff\xff\x01*&\n\tDirection\x12\x08\n\x04NONE\x10\x00\x12\x06\n\x02IN\x10\x01\x12\x07\n\x03OUT\x10\x02*\xc0\x01\n\nOutputType\x12\t\n\x05GRAPH\x10\x00\x12\x07\n\x03\x41PP\x10\x01\x12\r\n\tBOUND_APP\x10\x02\x12\x0b\n\x07RESULTS\x10\x03\x12\n\n\x06TENSOR\x10\x04\x12\r\n\tDATAFRAME\x10\x05\x12\x13\n\x0fVINEYARD_TENSOR\x10\x06\x12\x16\n\x12VINEYARD_DATAFRAME\x10\x07\x12\x15\n\x11INTERACTIVE_QUERY\x10\x08\x12\x12\n\x0eLEARNING_GRAPH\x10\n\x12\x0f\n\x0bNULL_OUTPUT\x10\x65*\xc8\x06\n\rOperationType\x12\x10\n\x0c\x43REATE_GRAPH\x10\x00\x12\x0c\n\x08\x42IND_APP\x10\x01\x12\x0e\n\nCREATE_APP\x10\x02\x12\x13\n\x0fMODIFY_VERTICES\x10\x03\x12\x10\n\x0cMODIFY_EDGES\x10\x04\x12\x0b\n\x07RUN_APP\x10\x05\x12\x0e\n\nUNLOAD_APP\x10\x06\x12\x10\n\x0cUNLOAD_GRAPH\x10\x07\x12\x0f\n\x0bREPARTITION\x10\x08\x12\x13\n\x0fTRANSFORM_GRAPH\x10\t\x12\x10\n\x0cREPORT_GRAPH\x10\n\x12\x11\n\rPROJECT_GRAPH\x10\x0b\x12\x15\n\x11PROJECT_TO_SIMPLE\x10\x0c\x12\x0e\n\nCOPY_GRAPH\x10\r\x12\x10\n\x0c\x41\x44\x44_VERTICES\x10\x0e\x12\r\n\tADD_EDGES\x10\x0f\x12\x0e\n\nADD_LABELS\x10\x10\x12\x0f\n\x0bTO_DIRECTED\x10\x11\x12\x11\n\rTO_UNDIRECTED\x10\x12\x12\x0f\n\x0b\x43LEAR_EDGES\x10\x13\x12\x0f\n\x0b\x43LEAR_GRAPH\x10\x14\x12\x0e\n\nVIEW_GRAPH\x10\x15\x12\x13\n\x0fINDUCE_SUBGRAPH\x10\x16\x12\x12\n\x0eUNLOAD_CONTEXT\x10\x17\x12\x11\n\rARCHIVE_GRAPH\x10\x18\x12\x13\n\x0fSERIALIZE_GRAPH\x10\x19\x12\x15\n\x11\x44\x45SERIALIZE_GRAPH\x10\x1a\x12\x0c\n\x08SUBGRAPH\x10 \x12\x0f\n\x0b\x44\x41TA_SOURCE\x10.\x12\r\n\tDATA_SINK\x10/\x12\x14\n\x10\x43ONTEXT_TO_NUMPY\x10\x32\x12\x18\n\x14\x43ONTEXT_TO_DATAFRAME\x10\x33\x12\x16\n\x12TO_VINEYARD_TENSOR\x10\x35\x12\x19\n\x15TO_VINEYARD_DATAFRAME\x10\x36\x12\x0e\n\nADD_COLUMN\x10\x37\x12\x12\n\x0eGRAPH_TO_NUMPY\x10\x38\x12\x16\n\x12GRAPH_TO_DATAFRAME\x10\x39\x12\x17\n\x13REGISTER_GRAPH_TYPE\x10:\x12\x14\n\x10GET_CONTEXT_DATA\x10;\x12\n\n\x06OUTPUT\x10<\x12\x0e\n\nFROM_NUMPY\x10P\x12\x12\n\x0e\x46ROM_DATAFRAME\x10Q\x12\r\n\tFROM_FILE\x10R\x12\x15\n\x11GET_ENGINE_CONFIG\x10Z*\xd1\r\n\x08ParamKey\x12\x0e\n\nGRAPH_NAME\x10\x00\x12\x12\n\x0e\x44ST_GRAPH_NAME\x10\x01\x12\x0f\n\x0b\x43ONTEXT_KEY\x10\x02\x12\x0e\n\nGRAPH_TYPE\x10\x03\x12\x12\n\x0e\x44ST_GRAPH_TYPE\x10\x04\x12\x0c\n\x08OID_TYPE\x10\x05\x12\x0c\n\x08VID_TYPE\x10\x06\x12\x0f\n\x0bV_DATA_TYPE\x10\x07\x12\x0f\n\x0b\x45_DATA_TYPE\x10\x08\x12\x0e\n\nV_LABEL_ID\x10\t\x12\x0e\n\nE_LABEL_ID\x10\n\x12\r\n\tV_PROP_ID\x10\x0b\x12\r\n\tE_PROP_ID\x10\x0c\x12\x0f\n\x0bLINE_PARSER\x10\r\x12\n\n\x06\x45_FILE\x10\x0e\x12\n\n\x06V_FILE\x10\x0f\x12\x14\n\x10VERTEX_LABEL_NUM\x10\x10\x12\x12\n\x0e\x45\x44GE_LABEL_NUM\x10\x11\x12\x0c\n\x08\x44IRECTED\x10\x12\x12\x0e\n\nV_PROP_KEY\x10\x13\x12\x0e\n\nE_PROP_KEY\x10\x14\x12\x11\n\rV_DEFAULT_VAL\x10\x15\x12\x11\n\rE_DEFAULT_VAL\x10\x16\x12\x18\n\x14GRAPH_TEMPLATE_CLASS\x10\x17\x12\x18\n\x14REPARTITION_STRATEGY\x10\x18\x12\t\n\x05PARAM\x10\x1a\x12\x0f\n\x0b\x44ISTRIBUTED\x10\x1b\x12\x0f\n\x0bSCHEMA_PATH\x10\x1f\x12\x1d\n\x19GIE_GREMLIN_QUERY_MESSAGE\x10#\x12\x1f\n\x1bGIE_GREMLIN_REQUEST_OPTIONS\x10$\x12!\n\x1dGIE_GREMLIN_FETCH_RESULT_TYPE\x10%\x12\x11\n\rAPP_SIGNATURE\x10(\x12\x13\n\x0fGRAPH_SIGNATURE\x10)\x12\x17\n\x13IS_FROM_VINEYARD_ID\x10*\x12\x0f\n\x0bVINEYARD_ID\x10+\x12\x11\n\rVINEYARD_NAME\x10,\x12\x13\n\x0fVERTEX_MAP_TYPE\x10-\x12\x11\n\rCOMPACT_EDGES\x10.\x12\x14\n\x10USE_PERFECT_HASH\x10/\x12\x16\n\x12VERTEX_COLLECTIONS\x10\x33\x12\x14\n\x10\x45\x44GE_COLLECTIONS\x10\x34\x12\x0e\n\nGLE_HANDLE\x10<\x12\x0e\n\nGLE_CONFIG\x10=\x12\x12\n\x0eGLE_GEN_LABELS\x10>\x12\x0f\n\x0bIS_FROM_GAR\x10\x46\x12\x13\n\x0fGRAPH_INFO_PATH\x10G\x12\x0c\n\x08\x41PP_NAME\x10\x64\x12\x0c\n\x08\x41PP_ALGO\x10\x65\x12\x14\n\x10\x41PP_LIBRARY_PATH\x10\x66\x12\x11\n\rOUTPUT_PREFIX\x10g\x12\x10\n\x0cVERTEX_RANGE\x10h\x12\x0c\n\x08SELECTOR\x10i\x12\x08\n\x04\x41XIS\x10j\x12\x07\n\x03GAR\x10k\x12\x12\n\x0eTYPE_SIGNATURE\x10l\x12\x17\n\x13\x43MAKE_EXTRA_OPTIONS\x10m\x12\x10\n\x0bREPORT_TYPE\x10\xc8\x01\x12\x10\n\x0bMODIFY_TYPE\x10\xc9\x01\x12\t\n\x04NODE\x10\xca\x01\x12\t\n\x04\x45\x44GE\x10\xcb\x01\x12\x08\n\x03\x46ID\x10\xcc\x01\x12\x08\n\x03LID\x10\xcd\x01\x12\r\n\x08\x45\x44GE_KEY\x10\xce\x01\x12\n\n\x05NODES\x10\xcf\x01\x12\n\n\x05\x45\x44GES\x10\xd0\x01\x12\x0e\n\tCOPY_TYPE\x10\xd1\x01\x12\x0e\n\tVIEW_TYPE\x10\xd2\x01\x12\x1e\n\x19\x41RROW_PROPERTY_DEFINITION\x10\xac\x02\x12\r\n\x08PROTOCOL\x10\xad\x02\x12\x0b\n\x06VALUES\x10\xae\x02\x12\x08\n\x03VID\x10\xaf\x02\x12\x0c\n\x07SRC_VID\x10\xb0\x02\x12\x0c\n\x07\x44ST_VID\x10\xb1\x02\x12\n\n\x05LABEL\x10\xb2\x02\x12\x0e\n\tSRC_LABEL\x10\xb3\x02\x12\x0e\n\tDST_LABEL\x10\xb4\x02\x12\x0f\n\nPROPERTIES\x10\xb5\x02\x12\x0b\n\x06LOADER\x10\xb6\x02\x12\x12\n\rLOAD_STRATEGY\x10\xb7\x02\x12\x0c\n\x07ROW_NUM\x10\xb8\x02\x12\x0f\n\nCOLUMN_NUM\x10\xb9\x02\x12\x0e\n\tSUB_LABEL\x10\xbb\x02\x12\x11\n\x0cGENERATE_EID\x10\xbc\x02\x12\x15\n\x10\x44\x45\x46\x41ULT_LABEL_ID\x10\xbd\x02\x12\x08\n\x03GID\x10\xbe\x02\x12\x0f\n\nRETAIN_OID\x10\xbf\x02\x12\x14\n\x0fSTORAGE_OPTIONS\x10\xc1\x02\x12\x11\n\x0cREAD_OPTIONS\x10\xc2\x02\x12\x07\n\x02\x46\x44\x10\xc3\x02\x12\x0b\n\x06SOURCE\x10\xc4\x02\x12\x12\n\rWRITE_OPTIONS\x10\xc5\x02\x12\x0f\n\nCHUNK_NAME\x10\xd5\x02\x12\x0f\n\nCHUNK_TYPE\x10\xd6\x02\x12\x17\n\x12GRAPH_LIBRARY_PATH\x10\x90\x03\x12\x1d\n\x18GRAPH_SERIALIZATION_PATH\x10\x91\x03\x12\x0c\n\x07VFORMAT\x10\xf4\x03\x12\x0c\n\x07\x45\x46ORMAT\x10\xf5\x03\x12\x14\n\x0fJAVA_CLASS_PATH\x10\xf6\x03\x12\r\n\x08JVM_OPTS\x10\xf7\x03*~\n\nModifyType\x12\x10\n\x0cNX_ADD_NODES\x10\x00\x12\x10\n\x0cNX_ADD_EDGES\x10\x01\x12\x10\n\x0cNX_DEL_NODES\x10\x02\x12\x10\n\x0cNX_DEL_EDGES\x10\x03\x12\x13\n\x0fNX_UPDATE_NODES\x10\x04\x12\x13\n\x0fNX_UPDATE_EDGES\x10\x05*\xcd\x02\n\nReportType\x12\x0c\n\x08NODE_NUM\x10\x00\x12\x0c\n\x08\x45\x44GE_NUM\x10\x01\x12\x0c\n\x08HAS_NODE\x10\x02\x12\x0c\n\x08HAS_EDGE\x10\x03\x12\r\n\tNODE_DATA\x10\x04\x12\r\n\tEDGE_DATA\x10\x05\x12\x11\n\rSUCCS_BY_NODE\x10\x06\x12\x11\n\rPREDS_BY_NODE\x10\x07\x12\x11\n\rSELFLOOPS_NUM\x10\x08\x12\x18\n\x14NODE_ID_CACHE_BY_GID\x10\t\x12\x1a\n\x16NODE_ATTR_CACHE_BY_GID\x10\n\x12\x0f\n\x0bSUCC_BY_GID\x10\x0b\x12\x0f\n\x0bPRED_BY_GID\x10\x0c\x12\x14\n\x10SUCC_ATTR_BY_GID\x10\r\x12\x14\n\x10PRED_ATTR_BY_GID\x10\x0e\x12\x15\n\x11SUCC_ATTR_BY_NODE\x10\x0f\x12\x15\n\x11PRED_ATTR_BY_NODE\x10\x10\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_CLUSTERTYPE']._serialized_start=99
  _globals['_CLUSTERTYPE']._serialized_end=147
  _globals['_DATATYPE']._serialized_start=150
  _globals['_DATATYPE']._serialized_end=448
  _globals['_DIRECTION']._serialized_start=450
  _globals['_DIRECTION']._serialized_end=488
  _globals['_OUTPUTTYPE']._serialized_start=491
  _globals['_OUTPUTTYPE']._serialized_end=683
  _globals['_OPERATIONTYPE']._serialized_start=686
  _globals['_OPERATIONTYPE']._serialized_end=1526
  _globals['_PARAMKEY']._serialized_start=1529
  _globals['_PARAMKEY']._serialized_end=3274
  _globals['_MODIFYTYPE']._serialized_start=3276
  _globals['_MODIFYTYPE']._serialized_end=3402
  _globals['_REPORTTYPE']._serialized_start=3405
  _globals['_REPORTTYPE']._serialized_end=3738
  _globals['_QUERYARGS']._serialized_start=50
  _globals['_QUERYARGS']._serialized_end=97
# @@protoc_insertion_point(module_scope)
