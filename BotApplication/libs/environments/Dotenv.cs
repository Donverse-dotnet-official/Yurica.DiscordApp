namespace libs.environments;

public class Dotenv {

    private Configurations? _configurations;

    public Dotenv Configure(
        string path,
        bool removeWhitespace = true,
        bool removeQuotes = true
    ) {
        _configurations = new Configurations
        {
            Path = path,
            RemoveWhitespace = removeWhitespace,
            RemoveQuotes = removeQuotes
        };

        return this;
    }

    public Dotenv Load() {
        if (_configurations == null) {
            throw new InvalidOperationException("Dotenv is not configured.");
        }

        if (_configurations.Path == null) {
            throw new InvalidOperationException("Path is not configured.");
        }

        if (!File.Exists(_configurations.Path)) {
            throw new FileNotFoundException("File not found.", _configurations.Path);
        }

        var lines = File.ReadAllLines(_configurations.Path);
        foreach (var line in lines) {
            var parts = line.Split("=");
            if (parts.Length != 2) {
                continue;
            }

            var key = parts[0];
            var value = parts[1];

            if (_configurations.RemoveWhitespace) {
                // Remove whitespace from key
                key = key.Trim();
                // Remove whitespace from value
                value = value.Trim();
            }

            if (_configurations.RemoveQuotes) {
                // Remove quotes from key
                if (key.StartsWith("\"") && key.EndsWith("\""))
                {
                    key = key.Substring(1, key.Length - 2);
                }

                if (key.StartsWith("'") && key.EndsWith("'"))
                {
                    key = key.Substring(1, key.Length - 2);
                }

                if (key.StartsWith("`") && key.EndsWith("`"))
                {
                    key = value.Substring(1, key.Length - 2);
                }

                // Remove quotes from value
                if (value.StartsWith("\"") && value.EndsWith("\"")) {
                    value = value.Substring(1, value.Length - 2);
                }

                if (value.StartsWith("'") && value.EndsWith("'")) {
                    value = value.Substring(1, value.Length - 2);
                }

                if (value.StartsWith("`") && value.EndsWith("`")) {
                    value = value.Substring(1, value.Length - 2);
                }
            }

            Environment.SetEnvironmentVariable(key, value);
        }

        return this;
    }

    public string? GetValue(string key) {
        return Environment.GetEnvironmentVariable(key);
    }
}
