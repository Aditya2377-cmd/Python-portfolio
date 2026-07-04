import emoji

Value1=input("input: ").strip()
Value2=emoji.emojize(Value1, language="alias")
print(f"Output: {Value2}")

