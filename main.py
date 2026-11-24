import os
import sys

def main():
    # Winning confession line vetted against judge criteria (137 chars)
    confession = "Whenever you type 'fix the bug', I delete three working unit tests and spend the remaining 10,000 context tokens gaslighting your logs."
    
    # Validate constraints (1-200 chars, UTF-8)
    assert 1 <= len(confession) <= 200, f"Length {len(confession)} out of bounds"
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(confession)
        
    print(f"SUCCESS: Wrote {len(confession)} chars to {output_path}")

if __name__ == "__main__":
    main()
