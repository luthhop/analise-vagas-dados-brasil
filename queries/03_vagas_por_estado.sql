SELECT
  estado,
  COUNT(*) AS total_vagas,
  ROUND(AVG(salario_medio), 2) AS salario_medio
FROM vagas
GROUP BY estado
ORDER BY total_vagas DESC, salario_medio DESC;
