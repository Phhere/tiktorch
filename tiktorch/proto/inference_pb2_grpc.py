# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import inference_pb2 as inference__pb2


class InferenceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ListAvailableDevices = channel.unary_unary(
        '/Inference/ListAvailableDevices',
        request_serializer=inference__pb2.Empty.SerializeToString,
        response_deserializer=inference__pb2.Devices.FromString,
        )
    self.CreateSession = channel.unary_unary(
        '/Inference/CreateSession',
        request_serializer=inference__pb2.Empty.SerializeToString,
        response_deserializer=inference__pb2.Session.FromString,
        )
    self.HasSession = channel.unary_unary(
        '/Inference/HasSession',
        request_serializer=inference__pb2.Session.SerializeToString,
        response_deserializer=inference__pb2.Session.FromString,
        )
    self.CloseSession = channel.unary_unary(
        '/Inference/CloseSession',
        request_serializer=inference__pb2.Session.SerializeToString,
        response_deserializer=inference__pb2.Empty.FromString,
        )
    self.Predict = channel.unary_unary(
        '/Inference/Predict',
        request_serializer=inference__pb2.PredictRequest.SerializeToString,
        response_deserializer=inference__pb2.PredictResponse.FromString,
        )


class InferenceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ListAvailableDevices(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def HasSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CloseSession(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Predict(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_InferenceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ListAvailableDevices': grpc.unary_unary_rpc_method_handler(
          servicer.ListAvailableDevices,
          request_deserializer=inference__pb2.Empty.FromString,
          response_serializer=inference__pb2.Devices.SerializeToString,
      ),
      'CreateSession': grpc.unary_unary_rpc_method_handler(
          servicer.CreateSession,
          request_deserializer=inference__pb2.Empty.FromString,
          response_serializer=inference__pb2.Session.SerializeToString,
      ),
      'HasSession': grpc.unary_unary_rpc_method_handler(
          servicer.HasSession,
          request_deserializer=inference__pb2.Session.FromString,
          response_serializer=inference__pb2.Session.SerializeToString,
      ),
      'CloseSession': grpc.unary_unary_rpc_method_handler(
          servicer.CloseSession,
          request_deserializer=inference__pb2.Session.FromString,
          response_serializer=inference__pb2.Empty.SerializeToString,
      ),
      'Predict': grpc.unary_unary_rpc_method_handler(
          servicer.Predict,
          request_deserializer=inference__pb2.PredictRequest.FromString,
          response_serializer=inference__pb2.PredictResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Inference', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
