import argparse, json, random

STYLES = {
    "realistic": ["photorealistic", "8k uhd", "dslr photo", "high detail"],
    "anime": ["anime style", "cel shading", "vibrant colors"],
    "oil": ["oil painting", "thick brushstrokes", "impressionist"],
    "3d": ["3d render", "octane render", "volumetric lighting"],
}
QUALITY = ["masterpiece", "best quality", "highly detailed", "trending on artstation"]

def gen(concept, style="realistic", count=10):
    mods = STYLES.get(style, STYLES["realistic"])
    prompts = []
    for _ in range(count):
        m = random.sample(mods, min(3, len(mods)))
        q = random.sample(QUALITY, 2)
        prompts.append({"prompt": f"{concept}, {chr(44).join(m)}, {chr(44).join(q)}", "negative": "blurry, low quality, distorted"})
    return prompts

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--concept", required=True)
    p.add_argument("--style", default="realistic", choices=list(STYLES.keys()))
    p.add_argument("--count", type=int, default=10)
    p.add_argument("--output", default="prompts.json")
    a = p.parse_args()
    prompts = gen(a.concept, a.style, a.count)
    with open(a.output, "w") as f:
        json.dump(prompts, f, indent=2)
    print(f"Generated {len(prompts)} prompts -> {a.output}")

if __name__ == "__main__":
    main()
