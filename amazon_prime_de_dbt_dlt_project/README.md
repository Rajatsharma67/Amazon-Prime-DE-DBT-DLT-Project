# Amazon Prime DBT DLT Project

This dbt project transforms Amazon Prime data through a layered warehouse flow:

- `source/` contains source definitions.
- `standard_layer/` holds the cleaned/raw staging model.
- `target_layer/` contains the final transformed model.

## Run

From the project directory, use:

```bash
dbt parse
dbt run --target dev
dbt run --target prod
dbt test
```
