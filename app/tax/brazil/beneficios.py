# -*- coding: utf-8 -*-
import datetime


def fgts_calculator(months_worked, salary):
    """
    Essa função serve para calcular o FGTS, FGTS que é o valor
    que de 8% que é retirado do salário do trabalhador todo mês
    e na demissão é devolvido ao trabalhador.
    Args:
        months_worked: É o numero de meses trabalhados da pessoa.
        salary: É o salário bruto da pessoa.
    Return:
        Essa função vai retornar o valor final do calculo do FGTS.
    """
    i = 0
    result = 0
    while i < months_worked:
        result += salary * 0.08
        i = i + 1
    return result


def months_worked_calculator(star_year, star_month, end_year, end_month):
    """
    Essa função serve para pegar as informações da data de contratação
    e demissão, e calcular por quantos meses de fgts a pessoa teve.
    Args:
        star_year: Ano da contratação da pessoa.
        star_month: Mês de contratação da pessoa.
        end_year: Ano da demissão da pessoa.
        end_month: Mês da demissão da pessoa.
    Return:
        Essa função vai retornar a diferênça de meses entre a contratação e demissão.
    """
    month_of_hiring = datetime.datetime(star_year, star_month, 1)
    month_of_dismissal = datetime.datetime(end_year, end_month, 1)
    months_worked = (month_of_dismissal.year - month_of_hiring.year) * 12 + (
        month_of_dismissal.month - month_of_hiring.month
    )
    return months_worked + 1


def date_string_converter(
    date_string_month_of_hiring, date_string_month_of_dismissal
):
    """
    Essa função serve para converter uma string da data no modelo dd/mm/yyyy para os
    meses e anos em valor inteiro para calculo.
    Args:
        date_string_month_of_hiring: Data por extenso em string da contratação.
        date_string_month_of_dismissal: Data por extenso em string da demissão.
    Return:
        Essa função vai retornar os valores inteiros da dos anos e meses da contratação
        e demissão.
    """
    date_splited_start = date_string_month_of_hiring.split('/')
    date_splited_end = date_string_month_of_dismissal.split('/')

    star_year = int(date_splited_start[1])
    star_month = int(date_splited_start[2])
    end_year = int(date_splited_end[1])
    end_month = int(date_splited_end[2])

    return star_year, star_month, end_year, end_month
