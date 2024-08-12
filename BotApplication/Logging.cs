using Discord;

namespace BotApplication;

public class Logging
{
    public static Task Log(LogMessage msg)
    {
        var content = msg.Exception is not null ? msg.Exception.ToString() : msg.Message;
        var dateTime = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
        Console.WriteLine($"[{dateTime}] [{msg.Source}] [{msg.Severity}] {content}");
        return Task.CompletedTask;
    }
}
