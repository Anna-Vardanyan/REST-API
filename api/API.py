from fastapi import FastAPI, HTTPException, Depends, Query, status
from sqlalchemy.orm import Session
from sqlalchemy import func, and_, exists, select, asc, desc, text
from typing import List, Dict
import Schemas
from TablesInitScript import Base, Operator, Subscriber, Connection, init_db

app = FastAPI()

db_session = init_db()

def get_db():
    db = db_session
    try:
        yield db
    finally:
        db.close()


@app.post("/operators/", status_code=status.HTTP_201_CREATED, response_model=Schemas.Operator)
def create_operator(operator: dict, db: Session = Depends(get_db)):
    try:
        db_operator = Operator(**operator)
        db.add(db_operator)
        db.commit()
        db.refresh(db_operator)
        return db_operator
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating operator: {str(e)}")

@app.get("/operators/", response_model=List[Schemas.Operator])
def list_operators(
        page: int = 0,
        page_size: int = 10,
        sort_by: str = None,
        sort_direction: str = 'asc',
        db: Session = Depends(get_db)
):
    query = db.query(Operator)
    if sort_by:
        if not hasattr(Operator, sort_by):
            raise HTTPException(status_code=400, detail=f"Invalid sort field: {sort_by}")
        sort_column = getattr(Operator, sort_by)
        if sort_direction == 'desc':
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))
    operators = query.offset(page * page_size).limit(page_size).all()
    return operators

@app.get("/operators/{operator_id}", response_model=Schemas.Operator)
def get_operator(operator_id: int, db: Session = Depends(get_db)):
    operator = db.query(Operator).filter(Operator.id == operator_id).first()
    if not operator:
        raise HTTPException(status_code=404, detail="Operator not found")
    return operator

@app.put("/operators/{operator_id}", response_model=Schemas.Operator)
def update_operator(operator_id: int, operator: Schemas.OperatorCreate, db: Session = Depends(get_db)):
    db_operator = db.query(Operator).filter(Operator.id == operator_id).first()
    if not db_operator:
        raise HTTPException(status_code=404, detail="Operator not found")
    for key, value in operator.items():
        setattr(db_operator, key, value)
    db.commit()
    db.refresh(db_operator)
    return db_operator

@app.delete("/operators/{operator_id}")
def delete_operator(operator_id: int, db: Session = Depends(get_db)):
    db_operator = db.query(Operator).filter(Operator.id == operator_id).first()
    if not db_operator:
        raise HTTPException(status_code=404, detail="Operator not found")
    db.delete(db_operator)
    db.commit()
    return {"message": "Operator deleted successfully"}


@app.post("/subscribers/", status_code=status.HTTP_201_CREATED, response_model=Schemas.Subscriber)
def create_subscriber(subscriber: dict, db: Session = Depends(get_db)):
    try:
        db_subscriber = Subscriber(**subscriber)
        db.add(db_subscriber)
        db.commit()
        db.refresh(db_subscriber)
        return db_subscriber
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating operator: {str(e)}")

@app.get("/subscribers/", response_model=List[Schemas.Subscriber])
def list_subscribers(
        page: int = 0,
        page_size: int = 10,
        sort_by: str = None,
        sort_direction: str = 'asc',
        db: Session = Depends(get_db)
):
    query = db.query(Subscriber)
    if sort_by:
        if not hasattr(Subscriber, sort_by):
            raise HTTPException(status_code=400, detail=f"Invalid sort field: {sort_by}")
        sort_column = getattr(Subscriber, sort_by)
        if sort_direction == 'desc':
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))
    subscribers = query.offset(page * page_size).limit(page_size).all()
    return subscribers

@app.get("/subscribers/{subscriber_id}", response_model=Schemas.Subscriber)
def get_subscriber(subscriber_id: int, db: Session = Depends(get_db)):
    subscriber = db.query(Subscriber).filter(Subscriber.id == subscriber_id).first()
    if not subscriber:
        raise HTTPException(status_code=404, detail="Subscriber not found")
    return subscriber

@app.put("/subscribers/{subscriber_id}", response_model=Schemas.Subscriber)
def update_subscriber(subscriber_id: int, subscriber: dict, db: Session = Depends(get_db)):
    db_subscriber = db.query(Subscriber).filter(Subscriber.id == subscriber_id).first()
    if not db_subscriber:
        raise HTTPException(status_code=404, detail="Subscriber not found")
    for key, value in subscriber.items():
        setattr(db_subscriber, key, value)
    db.commit()
    db.refresh(db_subscriber)
    return db_subscriber

@app.delete("/subscribers/{subscriber_id}")
def delete_subscriber(subscriber_id: int, db: Session = Depends(get_db)):
    db_subscriber = db.query(Subscriber).filter(Subscriber.id == subscriber_id).first()
    if not db_subscriber:
        raise HTTPException(status_code=404, detail="Subscriber not found")
    db.delete(db_subscriber)
    db.commit()
    return {"message": "Subscriber deleted successfully"}


@app.post("/connections/", status_code=status.HTTP_201_CREATED, response_model=Schemas.Connection)
def create_connection(connection: dict, db: Session = Depends(get_db)):
    try:
        db_connection = Connection(**connection)
        db.add(db_connection)
        db.commit()
        db.refresh(db_connection)
        return db_connection
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error creating operator: {str(e)}")

@app.get("/connections/", response_model=List[Schemas.Connection])
def list_connections(
        page: int = 0,
        page_size: int = 10,
        sort_by: str = None,
        sort_direction: str = 'asc',
        db: Session = Depends(get_db)
):
    query = db.query(Connection)
    if sort_by:
        if not hasattr(Connection, sort_by):
            raise HTTPException(status_code=400, detail=f"Invalid sort field: {sort_by}")
        sort_column = getattr(Connection, sort_by)
        if sort_direction == 'desc':
            query = query.order_by(desc(sort_column))
        else:
            query = query.order_by(asc(sort_column))
    connections = query.offset(page * page_size).limit(page_size).all()
    return connections

@app.get("/connections/{connection_id}", response_model=Schemas.Connection)
def get_connection(connection_id: int, db: Session = Depends(get_db)):
    connection = db.query(Connection).filter(Connection.id == connection_id).first()
    if not connection:
        raise HTTPException(status_code=404, detail="Connection not found")
    return connection

@app.put("/connections/{connection_id}", response_model=Schemas.Connection)
def update_connection(connection_id: int, connection: dict, db: Session = Depends(get_db)):
    db_connection = db.query(Connection).filter(Connection.id == connection_id).first()
    if not db_connection:
        raise HTTPException(status_code=404, detail="Connection not found")
    for key, value in connection.items():
        setattr(db_connection, key, value)
    db.commit()
    db.refresh(db_connection)
    return db_connection

@app.delete("/connections/{connection_id}")
def delete_connection(connection_id: int, db: Session = Depends(get_db)):
    db_connection = db.query(Connection).filter(Connection.id == connection_id).first()
    if not db_connection:
        raise HTTPException(status_code=404, detail="Connection not found")
    db.delete(db_connection)
    db.commit()
    return {"message": "Connection deleted successfully"}


#5 queries task

#SELECT ... WHERE ...
@app.get("/operators/all/filter", response_model=List[Schemas.Operator])
def list_operators_with_conditions(
    name_contains: str = None,
    number_count_min: int = None,
    page: int = 0,
    page_size: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(Operator)
    if name_contains:
        query = query.filter(Operator.name.contains(name_contains))
    if number_count_min is not None:
        query = query.filter(Operator.number_count >= number_count_min)
    operators = query.offset(page * page_size).limit(page_size).all()
    return operators

#JOIN
@app.get("/connections/all/joined", response_model=List[Dict])
def join_operators_and_subscribers(page: int = 0, page_size: int = 50, db: Session = Depends(get_db)):
    joined_query = db.query(
        Operator.name.label("operator_name"),
        Subscriber.full_name.label("subscriber_name"),
        Connection.installation_date
    ).join(Connection, Connection.operator_id == Operator.id)
    joined_query = joined_query.join(Subscriber, Connection.subscriber_id == Subscriber.id)
    joined_query = joined_query.offset(page * page_size).limit(page_size)
    results = joined_query.all()
    combined = [
        {
            "operator_name": row.operator_name,
            "subscriber_name": row.subscriber_name,
            "installation_date": row.installation_date
        }
        for row in results
    ]
    return combined

#UPDATE ...
@app.put("/connections/{connection_id}/conditional", response_model=Schemas.Connection)
def update_connection_with_condition(
    connection_id: int,
    update_data: dict,
    debt_threshold: float = 50,
    number_count_threshold: int = 3000,
    db: Session = Depends(get_db)
):
    connection = db.query(Connection).filter(Connection.id == connection_id).first()
    if not connection:
        raise HTTPException(status_code=404, detail="Connection not found")
    condition_query = db.query(Connection).filter(
        and_(
            Connection.id == connection_id,
            Connection.debt < debt_threshold,
            exists(
                select(Operator.id)
                .where(Operator.id == Connection.operator_id)
                .where(Operator.number_count > number_count_threshold)
            )
        )
    )
    if not db.query(condition_query.exists()).scalar():
        raise HTTPException(
            status_code=400,
            detail=f"Condition not met: Debt must be < {debt_threshold} and associated operator must have more than {number_count_threshold} numbers."
        )
    for key, value in update_data.items():
        setattr(connection, key, value)
    db.commit()
    db.refresh(connection)
    return connection

#GROUP BY
@app.get("/connections/all/grouped", response_model=Dict[str, int])
def group_connections_by_status(db: Session = Depends(get_db)):
    grouped = db.query(Connection.tariff_plan, func.count(Connection.id))
    grouped = grouped.group_by(Connection.tariff_plan).all()
    return {tariff_plan: count for tariff_plan, count in grouped}


#GIN INDEX SEARCH
@app.get("/search_meta_data")
def search_metadata(query: str, db: Session = Depends(get_db)):
    search_query = text('SELECT * FROM "connection" WHERE "meta_data"::text ~ :query')
    results = db.execute(search_query, {"query": query}).fetchall()
    return {"results": [dict(result._mapping) for result in results]}