from transformers import GPTNeoForCausalLM, GPT2Tokenizer


def load_model(model_path):
    # Load the model and tokenizer
    model = GPTNeoForCausalLM.from_pretrained(model_path)
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    return model, tokenizer


if __name__ == "__main__":
    model_path = "C:\\Users\\shubh\\OneDrive\\Desktop\\Hyperboost\\gpt-neo-125m"
    model, tokenizer = load_model(model_path)
    print("Model loaded successfully!")
