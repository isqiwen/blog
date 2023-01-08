import pynecone as pc


config = pc.Config(
    app_name="blog",
    bun_path="$HOME/.bun/bin/bun",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=[
        "react-confetti",
        "react-colorful",
        "react-copy-to-clipboard",
    ],
)
