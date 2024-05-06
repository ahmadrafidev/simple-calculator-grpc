import grpc
import calculator_pb2
import calculator_pb2_grpc

def add(num1, num2):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(num1=num1, num2=num2))
    print(f"Result: {response.result}")

def subtract(num1, num2):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Subtract(calculator_pb2.SubtractRequest(num1=num1, num2=num2))
    print(f"Result: {response.result}")

def multiply(num1, num2):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Multiply(calculator_pb2.MultiplyRequest(num1=num1, num2=num2))
    print(f"Result: {response.result}")

def divide(num1, num2):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Divide(calculator_pb2.DivideRequest(num1=num1, num2=num2))
    print(f"Result: {response.result}")

def square_root(num):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.SquareRoot(calculator_pb2.SquareRootRequest(num=num))
    print(f"Result: {response.result}")

if __name__ == '__main__':
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")

    operation = input("Enter operation number (1/2/3/4/5): ")

    if operation in ['1', '2', '3', '4']:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if operation == '1':
            add(num1, num2)
        elif operation == '2':
            subtract(num1, num2)
        elif operation == '3':
            multiply(num1, num2)
        elif operation == '4':
            divide(num1, num2)
    elif operation == '5':
        num = float(input("Enter number: "))
        square_root(num)
    else:
        print("Invalid operation number.")