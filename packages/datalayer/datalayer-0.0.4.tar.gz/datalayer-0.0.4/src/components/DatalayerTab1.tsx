import { Text } from '@primer/react';

const Tab = (props: {version: string}): JSX.Element => {
  const { version } = props;
  return (
    <>
      <Text>Version: {version}</Text>
    </>
  );
};

export default Tab;
