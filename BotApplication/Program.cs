using libs.environments;

namespace BotApplication;

public class Program
{
    public static async Task Main(string[] args)
    {
        Dotenv dotenv = new Dotenv().Configure(".env/.env").Load();

        var discordClient = new DiscordClient()
            .Configure(int.Parse(dotenv.GetValue("SHARD_ID") ?? "0"), int.Parse(dotenv.GetValue("SHARD_TOTAL") ?? "1"))
            .LoginAsync(dotenv.GetValue("DISCORD_TOKEN") ?? string.Empty);

        await Task.Delay(-1);
        await Task.CompletedTask;
    }
}
