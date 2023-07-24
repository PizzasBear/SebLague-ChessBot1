# SebLague-ChessBot1
This is my bot for the challenge. It uses standard alpha-beta pruning with some tweaks, with a variant of the [CPW's Simplified Evaluation Function](https://www.chessprogramming.org/Simplified_Evaluation_Function).

I wrote a python script to compress byte arrays into as few C# tokens as possible (a bit less than 8 bytes per token). I used this to store the piece square tables. I'd be happy to see this getting used by other challenge entries. Here's how to use it:
```csharp
static byte[] bytes = BigInteger.Parse(/* your dollar string here */).ToByteArray(true, true);
```

## [Chess Coding Challenge (C#)](https://github.com/SebLague/Chess-Challenge/)
Welcome to the [chess coding challenge](https://youtu.be/iScy18pVR58)! This is a friendly competition in which your goal is to create a small chess bot (in C#) using the framework provided in this repository.
Once submissions close, these bots will battle it out to discover which bot is best!

I will then create a video exploring the implementations of the best and most unique/interesting bots.
I also plan to make a small game that features these most interesting/challenging entries, so that everyone can try playing against them.
