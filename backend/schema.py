
from .table.account_user import AccountUser
from .table.owner_pokemon import OwnerPokemon
from pydantic import create_model, Field, BaseModel
from typing import Optional
from sqlalchemy.inspection import inspect
from typing import List, Dict, Any, Optional


#---------------------------------------------------------------------------#
# Código padrão para trazer todas as colunas de cada tabela, identificação da sua formatação, descriçao da coluna e obrigatoriedade de preenchimento
def bringAllCollumns(model_class):
    columns = inspect(model_class).c
    annotations = {}

    for column in columns:
        column_type = column.type.python_type  
        description = column.info.get("description", "Campo sem descrição")
        
        if column.nullable:
            column_type = Optional[column_type]  
            annotations[column.name] = (column_type, Field(None, description=description))

        else:
            annotations[column.name] = (column_type, Field(..., description=description))
 
    return create_model(f"{model_class.__name__}Schema_All", **annotations)

AccountUserSchema_All = bringAllCollumns(AccountUser)
OwnerPokemonSchema_All = bringAllCollumns(OwnerPokemon)


#---------------------------------------------------------------------------#
# Código padrão para trazer todas as colunas de cada tabela, com excessão das colunas de chave principal, identificação da sua formatação, 
# descriçao da coluna e obrigatoriedade de preenchimento
def bringOnlyNoPrimaryKeyCollumns(model_class):
    columns = inspect(model_class).c
    annotations = {}

    for column in columns:
        if not column.primary_key:
            column_type = column.type.python_type  
            description = column.info.get("description", "Campo sem descrição")
            
            if column.nullable:
                column_type = Optional[column_type]  
                annotations[column.name] = (column_type, Field(None, description=description))

            else:
                annotations[column.name] = (column_type, Field(..., description=description))
 
    return create_model(f"{model_class.__name__}Schema_No_Auto", **annotations)

AccountUserSchema_No_Auto = bringOnlyNoPrimaryKeyCollumns(AccountUser)
OwnerPokemonSchema_No_Auto = bringOnlyNoPrimaryKeyCollumns(OwnerPokemon)



#---------------------------------------------------------------------------#
# Código padrão para trazer apenas a coluna de chave principal, identificação da sua formatação, descriçao da coluna e obrigatoriedade de preenchimento
def bringOnlyPrimaryKey(model_class):
    columns = inspect(model_class).c
    annotations = {}

    for column in columns:
        if column.primary_key:
            column_type = column.type.python_type  
            description = column.info.get("description", "Campo sem descrição")
            
            if column.nullable:
                column_type = Optional[column_type]  
                annotations[column.name] = (column_type, Field(None, description=description))

            else:
                annotations[column.name] = (column_type, Field(..., description=description))
 
    return create_model(f"{model_class.__name__}Schema_PrimaryKey", **annotations)

AccountUserSchema_PrimaryKey = bringOnlyPrimaryKey(AccountUser)
OwnerPokemonSchema_PrimaryKey = bringOnlyPrimaryKey(OwnerPokemon)
