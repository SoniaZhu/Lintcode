public class StackWithTransactions
{
    private readonly Stack&gt; _transactions = new Stack&gt;();
    private readonly Stack _stack = new Stack();

    public void Push(T data)
    {
        if (_transactions.IsEmpty)
        {
            _stack.Push(data);
            return;
        }
        _transactions.Top().Push(data);
    }

    public void Pop()
    {
        if (_transactions.IsEmpty)
        {
            _stack.Pop();
            return;
        }
        _transactions.Top().Pop();
    }

    public T Top()
    {
        return _transactions.IsEmpty ? _stack.Top() : _transactions.Top().Top();
    }

    public void Begin()
    {
        _transactions.Push(new Stack());
    }

    public bool Rollback()
    {
        if (_transactions.IsEmpty) return false;
        _transactions.Pop();
        return true;
    }

    public bool Commit()
    {
        if (_transactions.IsEmpty) return false;
        var transaction = _transactions.Top();
        _transactions.Pop();

        var innerTransaction = _transactions.IsEmpty
            ? _stack
            : _transactions.Top();

        Stack.Append(Stack.Reverse(transaction), innerTransaction);

        return true;
    }
}
