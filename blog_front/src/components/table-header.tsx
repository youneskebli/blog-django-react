type TableHeaderProps = {
  fields: string[];
};

const TableHeader = ({ fields }: TableHeaderProps) => {
  return (
    <thead>
      <tr>
        {fields.map((field) => (
          <th key={field} className="font-bold">
            {field.replace("_", " ")}
          </th>
        ))}
      </tr>
    </thead>
  );
};

export default TableHeader;
