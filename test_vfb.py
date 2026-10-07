from vfb_connect import vfb

print("Conectando con Virtual Fly Brain...")

result = vfb.get_terms_by_region("fan-shaped body")

print(result)
