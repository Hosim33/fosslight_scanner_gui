import { FC } from 'react';
import Text from '../atoms/text/Text';
import { FossLogo } from '../atoms/SVGIcons';

const AppInitializer: FC = () => {
  return (
    <div className="fixed h-full w-full draggable">
      <div className="flex h-full w-full flex-col items-center justify-center gap-5">
        <FossLogo width={40} height={40} />
        <Text type="p400-m" color="white">
          Getting Ready...
        </Text>
      </div>
    </div>
  );
};

export default AppInitializer;
