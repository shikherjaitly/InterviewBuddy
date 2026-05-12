import functools
import time

def interview_logger(func):
    """A Decorator that Logs execution time and function metadata. """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if args and not args[0]:
            print("--- [LOG] Validation Failed: Empty Prompt ---")
            return None # We exit early and don't even call the function!
        
        print(f"--- [LOG] Executing technical check: {func.__name__} ---")
        start_time = time.time()

        result = func(*args, **kwargs) #Executing the actual funciton

        end_time = time.time()
        print(f"--- [LOG] Finished in {end_time - start_time:.4f}s ---")
        return result

    return wrapper  

@interview_logger
def simulate_ai_call(prompt: str):
    """Simulates a call to an LLM."""
    time.sleep(1.5) # Simulate network latency
    return f"AI Response to: {prompt}"

# Test it
print(simulate_ai_call("Explain Python decorators like I'm 5."))