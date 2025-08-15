with tb_freq_abs as (

    SELECT descCategoriaProduto,
            count(idTransacao) as FreqAbs

    from points
    GROUP BY descCategoriaProduto),

tb_freq_abs_acum as (

    select *,
            sum(FreqAbs) over (order by descCategoriaProduto) as FreqAbsAcum,
            1.0 * FreqAbs / (SELECT sum(FreqAbs) from tb_freq_abs) as FreqRelativa
    from tb_freq_abs
)

SELECT *,
        sum(FreqRelativa) over (ORDER by descCategoriaProduto) as FreqRelAcumulada
from tb_freq_abs_acum