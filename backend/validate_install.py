try:
    from transformers import GPTNeoForCausalLM, GPT2Tokenizer
    import torch
    import flask
    print("All modules are installed correctly.")
except ImportError as e:
    print(f"An error occurred: {e}")
