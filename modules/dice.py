from bot import bot
import random


@bot.command(pass_context=True)
async def r(ctx):
	msg = ctx.message
	dice = msg.content

	async def invalid():
		await bot.say("Invalid usage. Must use format dX. (X=4,6,8,20)")

	# Attempt to see if input is in the valid format.
	try:
		dice = dice[dice.index('d') + 1]
	except ValueError:
		await invalid()
		return

	res = roll_die(int(dice))

	await bot.say(f"{msg.author.mention}\nRolling d{dice}: **{res}**")


@bot.command(pass_context=True)
async def rr(ctx):
	msg = ctx.message
	parts = msg.split()
	print(parts)

	if not parts[1] or not parts[1].split('d'):
		await bot.say("Incorrect usage. Must use format NdX. (N=0+, X=4,6,8,20)")
	else:

		for _ in range(parts[1].split('d')[0]):
			await bot.say(f"{msg.author}\n")


def roll_die(sides):
	valid_dice = [4, 6, 8, 20]

	# Must be a valid dice choice.
	if sides not in valid_dice:
		return

	# Return a random value from 1-X
	return random.randint(1, sides)