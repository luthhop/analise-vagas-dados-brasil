from __future__ import annotations

from analyze import main as build_report
from load_sqlite import load_sqlite
from transform import transform


def main() -> None:
    transform()
    db_path = load_sqlite()
    build_report()
    print("Pipeline finalizado com sucesso.")
    print(f"Banco disponivel em: {db_path}")


if __name__ == "__main__":
    main()
