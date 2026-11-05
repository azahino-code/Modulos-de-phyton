#!/usr/bin/env python3
from ex3 import TransformationFactory as T


if __name__ == "__main__":
	factory = T()
	base = factory.create_base()
	evolved = factory.create_evolved()
	print(
    	"Testing Creature with transform capability\n",
    	" base\n",
    	f"{base.describe()}\n",
    	f"{base.attack()}\n",
    	f"{base.transform()}\n",
    	f"{base.attack()}\n",
    	f"{base.revert()}\n",
    	" evolved:\n"
		f"{evolved.describe()}\n",
		f"{evolved.attack()}\n",
		f"{evolved.transform()}\n",
		f"{evolved.attack()}\n",
		f"{evolved.revert()}",
		sep = ""
	)
