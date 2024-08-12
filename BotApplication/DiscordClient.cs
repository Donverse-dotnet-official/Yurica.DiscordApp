using Discord;
using Discord.WebSocket;

namespace BotApplication;

public class DiscordClient
{

    private DiscordSocketConfig? _config;
    public DiscordSocketClient? DiscordSocket { get; private set; }

    public DiscordClient Configure(int shardId = 0, int shardTotal = 1)
    {
        _config = new DiscordSocketConfig
        {
            LogLevel = LogSeverity.Info,
            MessageCacheSize = 100,
            AlwaysDownloadUsers = true,
            ConnectionTimeout = 30000,
            ShardId = shardId,
            TotalShards = shardTotal,
            GatewayIntents = GatewayIntents.All
        };

        DiscordSocket = new DiscordSocketClient(_config);
        DiscordSocket.Log += Logging.Log;

        DiscordSocket.Ready += async () =>
        {
            // Remove all commands
            await DiscordSocket.Rest.DeleteAllGlobalCommandsAsync();

            // Get all guilds
            foreach (var guild in DiscordSocket.Guilds)
            {
                // Remove all commands
                await guild.DeleteApplicationCommandsAsync();
            }
        };

        return this;
    }

    public async Task LoginAsync(string token, TokenType tokenType = TokenType.Bot)
    {
        if (DiscordSocket == null) {
            throw new InvalidOperationException("DiscordSocket is not configured.");
        }

        await DiscordSocket.LoginAsync(tokenType, token);
        await DiscordSocket.StartAsync();
    }
}
