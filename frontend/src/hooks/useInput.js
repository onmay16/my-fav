import { useCallback, useState } from "react";

const useInput = (initialValue) => {
    const [value, setValue] = useState(initialValue);
    const handler = useCallback((e) => {
        setValue(e.target.value);
    }, [value, setValue]);

    return [value, setValue, handler];
};

export default useInput;