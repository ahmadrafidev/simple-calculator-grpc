# Implementation of a gRPC Calculator in Python

This README provides a step-by-step guide to implementing a simple gRPC-based calculator in Python. The calculator will support basic arithmetic operations: addition, subtraction, multiplication, division, and square root.

## Prerequisites

1. **Python 3.6+**
2. **virtualenv** (optional but recommended for creating isolated Python environments)

## 1. Setup the Environment

1. Install virtualenv (if not already installed):
   ```sh
   pip install virtualenv
2. Create a virtual environment:
    ```sh
    virtualenv myenv
3. Activate the virtual environment:
   1. For Windows:
      ```sh
      myenv\Scripts\activate
   2. For Linux/Mac:
        ```sh
        source myenv/bin/activate
4. Install necessary packages:
   ```sh
   pip install grpcio grpcio-tools
    ```

## 2. Generate gRPC Code from the Proto File

1. Run the following command to generate the gRPC code:

    ```sh
    python -m grpc_tools.protoc -I. --python_out=--grpc_python_out=. calculator.proto
    ```

    This will generate two files: 
    1. calculator_pb2.py
    2. calculator_pb2_grpc.py.

2. Running the Server and Client

   1. Run the Server:
        ```
        python server.py
    2. Run the Client:
        ```
        python client.py
Enjoy the application!
