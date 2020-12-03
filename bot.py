import discord
import json
from discord.ext import commands
from sympy import *
import numpy as np

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def cmds(ctx):
    await ctx.send("det takes 1 matrix and returns int of its determinant")
    await ctx.send("rref takes 1 matrix and returns Reduced Row Echelon Form")
    await ctx.send("inverse takes 1 matrix and returns its inverse if possible")
    await ctx.send("nullspace takes 1 matrix and returns list of column vectors that span its null space")
    await ctx.send("egval takes 1 matrix and returns its eigenvalues with algebraic complexity")
    await ctx.send("matrixall returns everything for 1 matrix except eigen things")
    await ctx.send("egall returns only eigen things for 1 matrix")

@client.command()
async def matrixall(ctx, message):
    await rref(ctx, message)
    await det(ctx, message)
    await inverse(ctx, message)
    await nullspace(ctx, message)

@client.command()
async def egall(ctx, message):
    await egval(ctx, message)
    await egvec(ctx, message)

@client.command()
async def rref(ctx, message):
    matrixIn = json.loads(message)
    M = Matrix(matrixIn)
    M_rref = M.rref()
    await ctx.send("Reduced Row Echelon is: ```py\n {}```\n".format(np.array(M_rref[0])))

@client.command()    
async def inverse(ctx, message):
    matrixIn = json.loads(message)
    M = Matrix(matrixIn)
    await ctx.send("The inverse is: ")
    if int(M.det()) != 0:
        ans = M.inv()
        await ctx.send("```py\n {}```".format(np.array(ans)))
    else:
        await ctx.send("```py\n Determinant is 0 therefore not invertible```")

@client.command()    
async def det(ctx, message):
    matrixIn = json.loads(message)
    M = Matrix(matrixIn)
    M = M.det()
    await ctx.send("The determinant is: ```py\n {}```".format(M))

@client.command()    
async def nullspace(ctx, message):
    matrixIn = json.loads(message)
    M = Matrix(matrixIn)
    M = M.nullspace()
    await ctx.send("The nullspace is: ```py\n {}```".format(np.array(M)))

@client.command()    
async def egval(ctx, message):
    matrixIn = json.loads(message)
    M = Matrix(matrixIn)
    M = M.eigenvals()
    await ctx.send("The eigenvalues (in the order [ eigenvalue : algebraic multiplicity ]) are: ```py\n {}```".format(np.array(M)))

client.run("TOKEN REDACTED")
